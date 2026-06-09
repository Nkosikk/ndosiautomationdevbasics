import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;
import org.testng.annotations.AfterTest;
import org.testng.annotations.Test;

import java.time.Duration;

public class loginToNdosiWebsite {

    WebDriver driver;

    @Test
    public void LoginToMobileWebsiteTest() {

        driver = new ChromeDriver();

        driver.manage().window().maximize();

        driver.get("https://ndosisimplifiedautomation.vercel.app/");

        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

        // Click Login button
        WebElement loginButton = wait.until(
                ExpectedConditions.elementToBeClickable(
                        By.xpath("//button[contains(@class,'user-pill')]")
                )
        );
        loginButton.click();

        // Enter Email
        wait.until(
                ExpectedConditions.visibilityOfElementLocated(
                        By.id("login-email")
                )
        ).sendKeys("yolandamasiza@gmail.com");

        // Enter Password
        driver.findElement(By.id("login-password"))
                .sendKeys("Masiza@1988");

        // Submit Login
        driver.findElement(By.id("login-submit"))
                .click();

        // Verify welcome text
        String welcomeText = wait.until(
                ExpectedConditions.visibilityOfElementLocated(
                        By.xpath("//span[contains(text(),'back')]")
                )
        ).getText();

        Assert.assertEquals(welcomeText, "back,");

        // Click Learn
        wait.until(
                ExpectedConditions.elementToBeClickable(
                        By.cssSelector("button.nav-dropdown-trigger")
                )
        ).click();

// Click Learning Materials
        wait.until(
                ExpectedConditions.elementToBeClickable(
                        By.xpath("//span[text()='Learning Materials']")
                )
        ).click();

// Click Web Automation Basic Form
        wait.until(
                ExpectedConditions.elementToBeClickable(
                        By.xpath("//span[text()='Web Automation Basic Form']")
                )
        ).click();

// Expand Basic Form Requirements
        wait.until(
                ExpectedConditions.elementToBeClickable(
                        By.xpath("//summary")
                )
        ).click();

// Verify instructions expanded
        Assert.assertTrue(
                wait.until(
                        ExpectedConditions.visibilityOfElementLocated(
                                By.xpath("//*[contains(text(),'Login with your test user')]")
                        )
                ).isDisplayed()
        );
    }

    @AfterTest
    public void closeBrowser() {
        if (driver != null) {
            driver.quit();
        }
    }
}