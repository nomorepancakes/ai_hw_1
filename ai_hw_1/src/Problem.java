import java.util.LinkedList;
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
    
    public Problem(){
        s0 = new State();
        goal = new State();
        tempState = new State();
        
        stateList = new LinkedList();
        stateList.add(s0);
        
        goal.setGoal();     // set goal the goal state
    }
    
    public int funct(){     // Path Finder function
        // Generate state
        // Put it in the queue randomly
        s0.printState();
        
        tempState = s0.transition(2, 0);
        stateList.add(tempState);
        tempState.printState();
        
        
        tempState = tempState.transition(1, 0);
        if(tempState == null){
            System.out.println("naber");
        }
        stateList.add(tempState);
        tempState.printState();
        
        tempState = tempState.transition(2, 0);
        stateList.add(0, tempState);
        tempState.printState();
        
        tempState = new State();
        tempState = (State) stateList.get(0);
        /*
        tempState = s0.transition(1, 0);
        tempState.printState();
        
        tempState = s0.transition(0, 2);
        tempState.printState();*/
        return 0;
    }
}
