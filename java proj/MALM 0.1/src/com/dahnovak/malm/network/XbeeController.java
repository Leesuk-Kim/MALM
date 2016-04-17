package com.dahnovak.malm.network;

import java.util.HashMap;
import java.util.Timer;

import com.dahnovak.malm.MainController;
import com.dahnovak.malm.peasant.AbstractPeasant;
import com.digi.xbee.api.RemoteXBeeDevice;
import com.digi.xbee.api.XBeeDevice;
import com.digi.xbee.api.XBeeNetwork;
import com.digi.xbee.api.exceptions.XBeeException;
import com.digi.xbee.api.listeners.IDiscoveryListener;

/**
 * Xbee 관련 컨트롤러
 * timer를 받은 peasant instance는 자기 할 일 하고 다음 peasant에게 넘김
 * 이 Class는 반드시 한 개만 생성됩니다.
 * @author Leesuk Kim (Leesuk.kim425@gmail.com)
 *
 */
public class XbeeController {
	private static HashMap<String, AbstractPeasant> peasants;
	private static XBeeNetwork network;
	private static PeasantDiscoveryListener pdl;
	private static XBeeDevice xbc;
	private static XBeeDevice xbr;
	private static Timer timer;
	private static XbeeController instance;
	
	public static XbeeController getInstance() {
		if(instance == null){
			MainController mc = MainController.getInstance();
			instance = new XbeeController(mc.getXBC_PORT(), mc.getXBR_PORT(), mc.getXB_BAUDRATE());
		}
		return instance;
	}

	private XbeeController(String cport, String rport, int baudRate){
		xbc = new XBeeDevice(cport, baudRate);
		xbr = new XBeeDevice(rport, baudRate);
		pdl = new PeasantDiscoveryListener();
		network = xbc.getNetwork();
		network.addDiscoveryListener(pdl);
		peasants = new HashMap<String, AbstractPeasant>();
		timer	= new Timer(true);//XXX 이거 deamon으로 돌아감
	}
	
	/**xbee관련 control을 시작합니다.
	 * 일단, DB에서 peasant 정보를 가져옵니다.
	 */
	public void start() {
		network = xbc.getNetwork();
	}
	
	/**
	 * peasant의 device를 등록합니다.<br>
	 * 1. 찾는다.<br>
	 * 2. peasants에 등록한다.<br>
	 * 3. timer에 등록한다.<br>
	 * @param ni device serial code 서버에 저장된 시리얼코드
	 * @param addr64 XbeeAddress64bit. 시리얼 코드와 함께 서버에서 보내줄 것임.
	 */
	public void discoverDevice(String ni, String addr64){
		RemoteXBeeDevice rd;
		try {
			rd = network.discoverDevice(ni);
			if(rd.get64BitAddress().equals(addr64)){
			}
		} catch (XBeeException e) {
			e.printStackTrace();
		}
			
	}
	
	public class PeasantDiscoveryListener implements IDiscoveryListener {

		@Override
		public void deviceDiscovered(RemoteXBeeDevice discoveredDevice) {

		}

		@Override
		public void discoveryError(String error) {

		}

		@Override
		public void discoveryFinished(String error) {

		}
	}
}
