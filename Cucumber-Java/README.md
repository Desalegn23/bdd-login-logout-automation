# cucumber-java

Automated BDD tests for login & logout on saucedemo.com using Cucumber, Selenium, and JUnit 5.

## Prerequisites
- JDK 17+
- Maven
- Chrome browser

## Build & Run

```sh
mvn clean test
```

## Headless Mode

Set environment variable `CI=true` to run Chrome in headless mode.

```sh
CI=true mvn test
```

## Project Structure

- `src/test/java/features/login_logout.feature` — Gherkin scenarios
- `src/test/java/steps/LoginLogoutSteps.java` — Step definitions
- `src/test/java/util/WebDriverFactory.java` — Chrome WebDriver utility

## License

MIT
