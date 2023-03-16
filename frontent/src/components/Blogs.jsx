import React, { Component } from 'react';
import axios from 'axios';

class Blogs extends Component {
  constructor(props) {
    super(props);

    this.state = {
      data: []
    };
  }

  componentDidMount() {
    axios.get('http://localhost:8000/api/')
    .then(res => {
      const data = res.data;
      this.setState({data});
    })
  }

  render() {
    return (
      <div>
        { this.state.data.map(d => <div key={d.id}>{d.title}: {d.category}</div>)}
      </div>
    );
  }
}

export default Blogs;