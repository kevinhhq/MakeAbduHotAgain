import React from 'react';
import axios from 'axios';
import { Card, Button, Form } from 'antd';
import CustomForm from '../components/Form'

const formTailLayout = {
    labelCol: { span: 4 },
    wrapperCol: { span: 8, offset: 20},
};

class FoodDetail extends React.Component {
    
    state = {
        foods: {}
    }

    componentDidMount() {
        const foodID = this.props.match.params.foodID;
        axios.get(`http://127.0.0.1:8000/api/foods/${foodID}`)
        .then(res => {
            this.setState({
                foods: res.data
            });
        })
    }

    handleDelete = (event) => {
        const foodID = this.props.match.params.foodID;
        axios.delete(`http://127.0.0.1:8000/api/foods/${foodID}`);
        this.props.history.push('/');
        this.forceUpdate();
    }

    render() {
        const item = this.state.foods;
        const summary = item.foods_summary;

        return (
            <div>
                <Card title={item.Name} >
                    <h2> Source Type: </h2>


                        <p> {item.SourceType} </p>

                    <h2> Nutritions: </h2>

                        Carb: {item.Carbonhydrates} <br/>
                        Fiber: {item.Fiber} <br/>
                        Protein: {item.Protein} <br/>
                        Fat: {item.Fat}
                </Card><br />

                { 
                    typeof summary !== 'undefined' ?
                    <Card title="summary" >
                        Number of Carb source foods: {summary.Carbonhydrates} <br />
                        Number of Fiber source foods: {summary.Fiber} <br />
                        Number of Protein source foods: {summary.Protein} <br />
                        Number of Fat source foods: {
                            typeof summary.Fat !== 'undefined' ?
                            summary.Fat
                            :
                            "0"
                        } <br />
                    </Card>

                    :
                    <Card title="summary" >
                        "Loading..."
                    </Card>

                }

                <CustomForm requestType='put' foodID={this.props.match.params.foodID} btnText='Update'/>
                <Form onSubmit={this.handleDelete}>
                    <Form.Item {...formTailLayout} layout='inline'>
                        <Button type='danger' htmlType='submit'> Delete </Button>
                    </Form.Item>
                </Form>
            </div>
        )
    }
}

export default FoodDetail;