import './App.css';
import Scorecard from './scorecard';
function App() {
  return (
    <>
    <div style={{
      backgroundColor:'teal',
      textAlign:'center',
      padding:30
    }}>
     <h1>scorecard</h1>
     
    </div>
    <div>
      <h3 style={{textAlign:'center'}}>team-A</h3>
    <Scorecard/>
    </div>
   <div>
    <h3 style={{
      textAlign:"center"
    }}>team-B</h3>
    <Scorecard/>
    </div>
    </>
  );
}

export default App;
