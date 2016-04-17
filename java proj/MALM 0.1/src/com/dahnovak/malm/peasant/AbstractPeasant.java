package com.dahnovak.malm.peasant;

import java.util.TimerTask;

import com.digi.xbee.api.RemoteXBeeDevice;

/**
 * peasant의 Xbee 관련 function을 가지고 있습니다. peasant는 xbee가 아니기 떄문입니다.
 * 이 Class가 instance가 될 때는 {@link RemoteXBeeDevice}를 instance화 하면서 이녀석에 맞는 {@link PeasantTask}도 instance합니다.
 * @author Leesuk Kim (Leesuk.kim425@gmail.com)
 *
 */
public abstract class AbstractPeasant implements IPeasantSchedulable {
	protected RemoteXBeeDevice remoteDevice;
	protected PeasantTask peasantTask;

	public RemoteXBeeDevice getRemoteDevice() {
		return remoteDevice;
	}

	public AbstractPeasant(RemoteXBeeDevice remoteDevice){
		this.remoteDevice = remoteDevice;
		peasantTask = new PeasantTask(this);
	}
	
	
	/**
	 * Peasant의 TimerTask를 define.
	 * @author Leesuk Kim (Leesuk.kim425@gmail.com)
	 *
	 */
	public class PeasantTask extends TimerTask {
		private IPeasantSchedulable schedule;
		
		public IPeasantSchedulable getSchedule() {
			return schedule;
		}

		public PeasantTask(IPeasantSchedulable schedule){
			this.schedule = schedule;
		}

		@Override
		public void run() {
			schedule.task();
		}
	}
}