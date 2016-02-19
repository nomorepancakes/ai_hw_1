package ai_hw_1;

/**
 *
 * @author inciboduroglu
 */
public class Problem{
    public State s0;
    public State goal;
    
    public Problem(){
        s0 = new State();
        goal = new State();
        
        goal.setGoal();     // set goal the goal state
    }
    
    public int funct(){
        s0.printState();
        goal.printState();
        
        return 0;
    }
}
