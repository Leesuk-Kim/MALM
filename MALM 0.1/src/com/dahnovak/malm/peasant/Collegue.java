package com.dahnovak.malm.peasant;
/**
 * <b>Peasant to MALM Common Transmission Interface</b><br>
 * When a Peasant sends message to MALM, the XbeeController class passes message to specified peasant instance.
 * A MALM sends general information to SERVER via verifying UESR, PeasantID, Status when receives message from peasants
 * @author Leesuk Kim (Leesuk.kim425@gmail.com)
 *
 */
public interface Collegue {
	public String receiveMessage();
}
