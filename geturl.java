package com.bjs.seleniumDemo;

import org.openqa.selenium.chrome.ChromeDriver;

public class geturl {

	public static void main(String[] args) throws InterruptedException {
		// TODO Auto-generated method stub

	//	System.setProperty("webdriver.chrome.driver ", "C:\\Selenium Componenet\\chromedriver.exe");
	ChromeDriver driver=new ChromeDriver();
	String url="http://www.gmail.com/";
	driver.get(url);
    String curl = driver.getCurrentUrl();
    System.out.println(curl); 
	}

}
