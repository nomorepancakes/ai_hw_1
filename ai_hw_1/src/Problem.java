import java.util.LinkedList;
import java.util.ArrayList;
//package ai_hw_1;

/**
 *
 * @author inciboduroglu
 */
public class Problem{
    public State s0;
    public State goal;
    State tempState;
    
    public LinkedList stateList;
    
    int [][] transArray;
    
    boolean illegal;
    
    public Problem(){
        s0 = new State();
        goal = new State();
        tempState = new State();
        
        stateList = new LinkedList();
        stateList.add(s0);
        
        goal.setGoal();     // set goal the goal state
        
        illegal = false;
    }
    
    public int funct(){     // Path Finder function
        // Generate state
        // Put it in the queue randomly
        s0.printState();
        tempState = s0.transition(2, 0);
        stateList.add(tempState);
        tempState.printState();
        
        while (!tempState.equals(goal)){
            tempState = tempState.transition(2, 0);
            if(!checkState(tempState)){
                stateList.add(tempState);
                tempState.printState();
                
                //tempState = new State();
                break;
            }
        }
        
        return 0;
    }
    
    private boolean checkState(State s){
        if(s == null){
            System.out.println("illegal");
            return true;
        }
        
        return false;
    }
    
    private void initTransArray(){
        
    }
}
