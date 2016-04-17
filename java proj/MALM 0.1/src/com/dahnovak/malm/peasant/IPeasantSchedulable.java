package com.dahnovak.malm.peasant;

public interface IPeasantSchedulable {
	/**
	 * Timer의 scheduling에 의해 자기 task를 실행할 수 있는 순간이 되면, peasant는 자기의 schedule을 실행합니다.
	 * 이 인터페이스를 통해 각 peasant는 자기의 task를 정의할 수 있습니다.
	 */
	public void task();
}