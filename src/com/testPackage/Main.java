package com.testPackage;

import java.io.*;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;

public class Main {

    public static void main(String[] args) {
		URL stockData; //initialize the stock data variable
		try {
			stockData = new URL("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SPY&apikey=DEDSQFY460FDRASD&datatype=pdf&outputsize=compact"); //This is only stock data for SPY. Need to find a way to take this data and put into list
			URLConnection avConnect = stockData.openConnection();
			BufferedReader line = new BufferedReader(new InputStreamReader(avConnect.getInputStream()));

			String inputLine;
			while ((inputLine = line.readLine()) != null)
				System.out.println(inputLine);	//reads line from API line by line
			line.close();

		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
