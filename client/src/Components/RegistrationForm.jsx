import React, { useState} from 'react';
import { useNavigate } from 'react-router-dom';



const RegistrationForm = () => {
  
  const navigate = useNavigate();
  

  const [formdata, setformData] = useState({
    username: '',
    email: '',
    password: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setformData({
      ...formdata,
      [name]: value,
    });
  };

  const [passwordError, setpasswordError] = useState('');
  const [regestration, setRegestration] = useState(null)

  const handleNavigation = () => {
    navigate('/login');
  };

  const validateEmail = (email) => {
    const emailpattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailpattern.test(email);
  };

  const validatePassword = (password) => {
    const passwordpattern = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
    return passwordpattern.test(password);
  };
  const handleSubmit = async (event) => {
    event.preventDefault();

    // validate email before submit
    if (!validateEmail(formdata.email)) {
      alert('Please enter a valid email');
      return;
    }

    if (!validatePassword(formdata.password)) {
      setpasswordError(
        'Password must be 8 characters long and contain at least one letter and one number'
      );
    } else {
      setpasswordError(''); // clear previous error
    }

    console.log('Password is valid');

    try{
      const response =await fetch('https://flask-apidelivery.onrender.com/auth/register', {
        method:'POST',
        headers:{
          'Content-Type':'application/json',
        },
        body:JSON.stringify(formdata),

      });

      if(response.status === 200){
        setRegestration('success')
        // reg was success redirect to login
        navigate('/login')
      
      }

      else{
        const data =await response.json()
        console.log(data.message);
        setRegestration('Failure')
      }
    }catch(error){
      console.error('Error during registration:', error)
    }
  };


  return (
    <div>
      <section className="picture">
        <form className="registration-form" onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="exampleInputUsername" >Username</label>
            <input
              type="text"
              className="form-control"
              id="exampleInputUsername"
              aria-describedby="emailHelp"
              placeholder="Enter username"
              name="username"
              value={formdata.username}
              onChange={handleChange}
            />
          </div>
          <div className="form-group">
            <label htmlFor="exampleInputEmail1" >Email address</label>
            <input
              type="email"
              className="form-control"
              id="exampleInputEmail1"
              aria-describedby="emailHelp"
              placeholder="Enter email"
              name="email"
              value={formdata.email}
              onChange={handleChange}
            />
          </div>
          <div className="form-group">
            <label htmlFor="exampleInputPassword1" >Password</label>
            <input
              type="password"
              className="form-control"
              id="exampleInputPassword1"
              placeholder="Password"
              name="password"
              value={formdata.password}
              onChange={handleChange}
            />
                {passwordError && (
              <p className="error-message">{passwordError}</p>
            )}
           
          </div>

          <button type="submit" className="btns">
            Submit
          </button>
          {regestration === 'success' && (
            <p className='success-message'>Successful regestration!Please proceed to Login</p>
          )}
         
          <div >
                <small className="text-muted">
                    <p className='white-text'> Alredy have an account? <a class="ml-2" href='/login'> Login</a> </p> 
                </small>
                </div>
        </form>
      </section>
    </div>
  );
};

export default RegistrationForm;

