import React,{Component} from 'react'
import Dropdown from 'react-bootstrap/Dropdown';
import '../style/Recommend.css'
class Recommend extends Component{
    constructor(){
        super()
        this.handleCheck = this.handleCheck.bind(this);
        this.state={
            GoalDict:{
                'lose':['kfc',
                    'Taco Bell',
                    'Jurassic Grill',
                    'BBQ PREMIUM CHICKEN',
                    'Wingstop',
                    'Poke Lab',
                    'JJ Fish and Chicken',],
                'keep':['Panda Express',
                    'Burrito King',
                    'Ko Fusion Campus',
                    'Taco Motorizado',
                    'D.P. Dough',
                    'Windy City Express',
                    'Masijta Grill',
                    'Rosati s Pizza',
                    'The Dancing Dog Eatery',
                    'Niro s Gyros - University Ave',
                    'Qdoba Mexican Eats',
                    'Caribbean Grill Restaurant',
                    'Signature Grill',],
                'gain':['Siam Terrace',
                    'Ambar India',
                    'Manolo s Pizza & Empanadas',
                    'Golden Wok',
                    'Bangkok Thai Restaurant',
                    'Xinh Xinh Cafe',
                    'Four Breakfast & More',
                    'Basil Thai',
                    'Merry Ann s Diner',
                    'Salad Meister',
                    'Koh-i-noor Indian Restaurant and Lounge',],
            },
            Res:'',
        }
    }

    handleCheck(value){
        this.setState({
            Res:value,
        })
    }

    render() {
        const GoalDict=this.state.GoalDict;
        return(
            <div className="Recommend">
                <div className="Goal">
                    <Dropdown>
                        <Dropdown.Toggle variant="success" id="dropdown-basic">
                            Choose Goal
                        </Dropdown.Toggle>

                        <Dropdown.Menu >
                            <div className="bottom"><Dropdown.Item onClick={this.handleCheck.bind(this, GoalDict['lose'])}>Lose weight</Dropdown.Item></div>
                            <div className="bottom"><Dropdown.Item onClick={this.handleCheck.bind(this, GoalDict['keep'])}>Keep weight</Dropdown.Item></div>
                            <div className="bottom"><Dropdown.Item onClick={this.handleCheck.bind(this, GoalDict['gain'])}>Gain weight</Dropdown.Item></div>

                        </Dropdown.Menu>
                    </Dropdown>;
                </div>
                <ul className="Result">
                    <li>
                        {Object.keys(this.state.Res).map(res=>
                        <li >
                            <a href={"https://www.ubereats.com/en-US/search/?q="+this.state.Res[res]}>{this.state.Res[res]}</a>
                        </li>)}
                    </li>
                </ul>
            </div>
        )
    }
}

export default Recommend
