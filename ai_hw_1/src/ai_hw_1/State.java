package ai_hw_1;

/**
 *
 * @author inciboduroglu
 */
public class State {
    final int CANN_NUM = 3;
    final int MISS_NUM = 3;
    private int cannibal;
    private int missionary;
    private int boat;
    
    public State(){
        cannibal = 3;
        missionary = 3;
        boat = 0;   // 0 -> left, 1 -> right
    }
    
    public State transition(int numC, int numM){
        // parameters of transition: number of cannibals, number of missionaries
        State newState = new State();
        
        // Condition
        if (numC + numM > 2 || numC + numM < 1){
            System.out.println("Napiyon?");
            return null;
        }
        
        newState.setCannibal(numC);
        newState.setMissionary(numM);
        
        return newState;
    }
    /*
    public State getState(){
        return this;
    }*/
    
    // Get cannibals on the left
    public int getLeftCannibal(){
        return cannibal;
    }
    
    // Get cannibals on the right
    public int getRightCannibal(){
        return CANN_NUM - cannibal;
    }
    
    public int getLeftMissionary(){
        return missionary;
    }
    
    public int getRightMissionary(){
        return MISS_NUM - missionary;
    }
    
    public int getBoatLoc(){
        return boat;
    }
    /**
     * setCannibal
     * @param num 
     */
    private void setCannibal(int num){
        cannibal = num;
    }
    /**
     * setMissionary
     * @param num 
     */
    private void setMissionary(int num){
        missionary = num;
    }
}
