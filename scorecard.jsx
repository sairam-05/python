import React,{useState} from 'react'

const Scorecard = () => {
    const [runs,setRuns]=useState(0)
    const [wickets,setWickets]=useState(0)
    const [target,setTarget]=useState(0)
    const [overs,setOvers]=useState(0)
    const [balls,setBall]=useState(0)
 
     const handlewicket=()=>{
      setWickets(wickets+1)
     
    if (balls==6){
        setOvers(overs+1)
    }
    setBall(balls==6?0:balls+1)
}
    
     const handleruns=(run)=>{
        setRuns(runs+run)
    if (balls==6){
        setOvers(overs+1)
    }
    setBall(balls==6?0:balls+1)
        
     }
    
    
     
    
    return (
        <>
            
                <h1 class='alignment'>score:{runs}/{wickets}</h1>
                 <p>current overs:{overs}.{balls}</p>
                

            
        {
         wickets<10?
        <div>
            overs==20?
        <div style={{
            display:'flex',
            justifyContent:'space-around',
            
        }}>
            
            <button style={{
                padding:20
                
            }} onClick={()=>handleruns(6)}>six</button>
            <button onClick={()=>handleruns(4)}>four</button>
            <button onClick={()=>handleruns(2)}>two</button>
            <button onClick={()=>handleruns(1)}>one</button>
            <button onClick={()=>handleruns(1)}>dot</button>
            <button onClick={handlewicket}>wicket</button>
        </div>
           :
           <p>gameover</p>
        </div>
        :
        <p>Gameover</p>
        
    }
         </>
    )
}

export default Scorecard