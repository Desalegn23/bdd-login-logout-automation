package steps;

import io.cucumber.java.AfterAll;
import io.cucumber.java.BeforeAll;
import io.cucumber.java.en.*;
import org.openqa.selenium.*;
import org.openqa.selenium.support.ui.*;
import util.WebDriverFactory;

public class LoginLogoutSteps {
    private static WebDriver driver;
    private static WebDriverWait wait;
    private static final String BASE_URL = "https://www.saucedemo.com/";

    @BeforeAll
    public static void setUp() {
        driver = WebDriverFactory.create();
        wait = new WebDriverWait(driver, 10);
    }

    @AfterAll
    public static void tearDown() {
        if (driver != null) driver.quit();
    }

    @Given("I am on the login page")
    public void i_am_on_login_page() {
        driver.get(BASE_URL);
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("user-name")));
    }

    @When("I login with username {string} and password {string}")
    public void i_login_with_credentials(String username, String password) {
        driver.findElement(By.id("user-name")).sendKeys(username);
        driver.findElement(By.id("password")).sendKeys(password);
        driver.findElement(By.id("login-button")).click();
    }

    @Then("I should see the dashboard")
    public void i_should_see_dashboard() {
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.className("app_logo")));
        assert driver.getCurrentUrl().contains("inventory");
    }

    @Given("I am logged in as {string} with password {string}")
    public void i_am_logged_in(String username, String password) {
        i_am_on_login_page();
        i_login_with_credentials(username, password);
        i_should_see_dashboard();
    }

    @When("I logout")
    public void i_logout() {
        WebElement menuBtn = wait.until(ExpectedConditions.elementToBeClickable(By.id("react-burger-menu-btn")));
        menuBtn.click();
        WebElement logoutBtn = wait.until(ExpectedConditions.elementToBeClickable(By.id("logout_sidebar_link")));
        logoutBtn.click();
    }

    @Then("I should be redirected to the login page")
    public void i_should_be_redirected_to_login() {
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("login-button")));
        assert driver.getCurrentUrl().contains("saucedemo.com");
    }
}
