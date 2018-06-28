import React from 'react';
import Select from 'react-select';
import 'react-select/dist/react-select.css';



class SelectBox extends React.Component {
  state = {
    selectedOption: '',
  }
  handleChange = (selectedOption) => {
    this.setState({ selectedOption });
    // selectedOption can be null when the `x` (close) button is clicked
    if (selectedOption) {
      console.log(`Selected: ${selectedOption.label}`);
    }
  }
  render() {
    const { selectedOption } = this.state;

    return (
      <Select
		className="selectbox"
        name="form-field-name"
        value={selectedOption}
        onChange={this.handleChange}
        options={[
          { value: '46A', label: '46A' },
          { value: '145', label: '145' },
		  { value: '39A', label: '39A' },
        ]}
      />
    );
  }
}

export default SelectBox
