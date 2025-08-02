package util;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.chrome.ChromeDriver;

public class WebDriverFactory {
    public static WebDriver create() {
        ChromeOptions options = new ChromeOptions();
        if ("true".equalsIgnoreCase(System.getenv("CI"))) {
            options.addArguments("--headless=new");
        }
        options.addArguments("--window-size=1280,800");
        return new ChromeDriver(options);
    }
}
