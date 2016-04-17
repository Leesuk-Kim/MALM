package com.dahnovak.malm.network;

public class ServerController {
	private static String host, port;
	
	public ServerController(){
		
	}

	public static void setHost(String host) {
		ServerController.host = host;
	}

	public static void setPort(String port) {
		ServerController.port = port;
	}

	public void open(String host, String port){
		this.host = host;
		this.port = port;
	}
}
