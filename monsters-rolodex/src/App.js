import { Component } from 'react';
import './App.css';


class App extends Component {
  constructor () {
    super();
    this.state = {
      monsters: [],
      searchFeild: ''
    };
  }
  componentDidMount() {
    fetch('https://jsonplaceholder.typicode.com/users')
      .then((response) => {
        return response.json();
      })
      .then((users) => this.setState(() => {
        return { monsters: users }
      }
      ))
  }


  onSearchChange = (event) => {
    const searchFeild = event.target.value.toLocaleLowerCase();
    this.setState(() => {
      return { searchFeild };
    })
  };

  render() {

    const { monsters, searchFeild } = this.state;
    const { onSearchChange } = this;
    const filteredMonsters = monsters.filter((monster) => {
      return monster.name.includes(searchFeild);
    });
   
    return (
      <div className="App">
        <input className='search-bok'
          type='search'
          placeholder='search monsters'
          onChange={onSearchChange}
        />
        {filteredMonsters.map(x => <div key={x.id}>
          <h1> {x.name}</h1>
        </div>)}


      </div>
    );
  }

}
export default App;
