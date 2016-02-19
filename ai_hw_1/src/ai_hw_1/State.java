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
        boat = 0;   
    }
    //
    //  Methods
    //
    public boolean equals(State that){
        if(this.cannibal == that.cannibal &&
           this.missionary == that.missionary &&
           this.boat == that.boat){
            return true;
        }
        return false;
    }
    /**
     * set goal
     * @param s
     * @return 
     */
    public void setGoal(){
        this.setCannibal(0);
        this.setMissionary(0);
        this.setBoat(1);
        
        //return s;
    }
    
    /**
     * transition
     * @param numC
     * @param numM
     * @return 
     */
    public State transition(int numC, int numM){    // boat seysini yapmadik :*
        // parameters of transition: number of cannibals, number of missionaries
        State newState = new State();
        int leftM;
        int leftC;
        
        // Conditions
        if (numC + numM > 2 || numC + numM < 1){    // Max two people can be on the boat
            System.out.println("Napiyon?");
            return null;
        }
        
        if (boat == 0){     // Going right
            if(     this.getLeftCannibal()-numC > 0 &&      // If there is enough on the left
                    this.getLeftMissionary()-numM > 0 ){
                newState.setCannibal(this.getLeftCannibal() - numM);
                newState.setCannibal(this.getLeftCannibal() - numM);
            } else return null;
            
        }
        
        return newState;
    }
  
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
    
    public void printState(){
        System.out.println("Cannibals: \t" + cannibal + " | " + (CANN_NUM - cannibal) +
                            "\nMissionaries: \t" + missionary + " | " + (MISS_NUM - missionary) +
                            "\nBoat: \t\t" + boat);
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
    /**
     * set boat
     * @param num 
     */
    private void setBoat(int num){
        if (num >= 0 && num <= 1)
            boat = num;
    }
}
