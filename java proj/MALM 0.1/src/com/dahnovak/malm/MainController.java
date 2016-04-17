package com.dahnovak.malm;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Properties;

import com.dahnovak.malm.network.ServerController;
import com.dahnovak.malm.network.XbeeController;

/***
 * <b>start app</b>
 * initialize {@link ServerController}
 * 
 * @author Leesuk Kim (Leesuk.kim425@gmail.com)
 *
 */
public class MainController {
	public static ServerController serverController;
	public static XbeeController xbController;
	
	private static String SERVER_HOST = "192.168.0.1";
	private static String SERVER_PORT = "9645";
	private static String XBC_PORT = "COM8";
	private static String XBR_PORT = "COM7";
	private static int XB_BAUDRATE = 9600;
	private static MainController instance;
	
	private MainController(){
		//서버관리자 초기화. 서버 주소 입력 요망
		serverController = new ServerController();
		xbController	= XbeeController.getInstance();
		//sc랑 xbc는 쓰래드로 돌려야할 듯
		serverController.open(SERVER_HOST, SERVER_PORT);
		xbController.start();
	}
	
	public String getSERVER_HOST() {
		return SERVER_HOST;
	}

	public String getSERVER_PORT() {
		return SERVER_PORT;
	}

	public String getXBC_PORT() {
		return XBC_PORT;
	}

	public String getXBR_PORT() {
		return XBR_PORT;
	}

	public int getXB_BAUDRATE() {
		return XB_BAUDRATE;
	}

	public static MainController getInstance(){
		if(instance == null)
			instance = new MainController();
		return instance;
	}
	
	public static void main(String[] args) {
		Properties p = new Properties();
		try {
			p.load(new FileInputStream("cfg.ini"));
			
			SERVER_HOST = p.getProperty("server_host");
			SERVER_PORT = p.getProperty("server_port");
			XBC_PORT = p.getProperty("xbee_controller");
			XBR_PORT = p.getProperty("xbee_recruiter");
			XB_BAUDRATE = Integer.parseInt(p.getProperty("xbee_baudrate"));
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}