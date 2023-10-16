
import React, { useState,useEffect } from "react";
import { useParams } from 'react-router-dom';



function RestaurantMenu() {
  const [userData, setuserData] =useState({})
  const [menuItems, setMenuItems] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [selectedItem, setSelectedItem] = useState(null);
  const [showToast, setShowToast] = useState(false);
  const { restaurant_id } = useParams();
  


  useEffect(() => {
    // Fetch menu items for the specified restaurant based on restaurantId
    const fetchMenuItems = async () => {
      try {
        // Get the JWT token from wherever it is stored (e.g., localStorage)
        const accessToken = localStorage.getItem('accessToken');
  
        const response = await fetch(`http://127.0.0.1:5000/menus/restmenus/${restaurant_id}`, {
          method: 'GET',
          headers: {
            Authorization: `Bearer ${accessToken}`, // Include the JWT token in the headers
          },
        });
  
        if (response.status === 200) {
          const data = await response.json();
          setMenuItems(data);
          
        } else {
          console.error('Error fetching menu items');
        }
      } catch (error) {
        console.log('Error:', error);
      }
    };
  
    fetchMenuItems();

    const fetchdata =async () =>{
      try{
        const accessToken = localStorage.getItem('accessToken');
        const response = await fetch("http://127.0.0.1:5000/users/account",{
          method:'GET',
          headers:{
            'Authorization':`Bearer ${accessToken}`,
          },
        });
        if (response.status === 200){
          const data = await response.json();
          setuserData(data);
        }else if(response.status === 401){
          navigate('/login')
        } else {
          console.log('Error:', response.status);
        }
      }catch(error){
        console.error('Error:', error)
    } 
  };

    fetchdata();
  }, []);

  const handleOrderClick = (item) => {
    setSelectedItem(item);
    setShowModal(true);
  };

  const handleConfirmOrder = () => {
    setShowModal(false);
    setShowToast(true);
  };

  // variable to store the timer ID
  let toastTimer;

  // Clear the previous timer if any and set a new timer for hiding the toast after 5 seconds
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => {
    setShowToast(false);
  }, 5000);

  return (
    <div className="parentcontainer">
       <nav className='navbar'>
        <div className='logo'>
          <p>Food<span>.</span></p>
        </div>

        <div className="user-info">
          <div className="user-welcome">
            <i className="fas fa-user"></i>
            <p className='align'>{userData.username}</p>
          </div>
        </div>
      </nav>
    <div className="container">
      <h2 className="text-center mt-4 mb-4"> Menu</h2>
      <p style={{ textAlign: "center" }}>Menusto Delight Your Palate</p>
      <p style={{ textAlign: "center" }}>
        Before you savor the delectable array of main courses, we invite you to
        indulge in our delightful selection of appetizers. Our culinary team has
        carefully curated these mouthwatering starters to awaken your taste buds
        and set the stage for an exceptional dining experience. From light and
        refreshing salads to savory small plates and irresistible finger foods,
        our appetizers showcase a variety of flavors and textures that will
        leave you wanting more. Each dish is crafted with the finest
        ingredients, expertly seasoned and presented to perfection.
      </p>
      <p style={{ textAlign: "center" }}>
        From the Tasty Dishes team, we look forward to serving you the appetizer
        of your dreams. Bon appétit!
      </p>
      <div className="row">
        {menuItems.map((item) => (
          <div key={item.id} className="col-md-4 mb-4">
            <div className="card food-card h-100 ">
              <img
                src={item.image_url}
                alt={item.name}
                className="card-img-top"
                style={{ height: "200px", objectFit: "cover" }}
              />
              <div className="card-body" style={{fontSize:"15px"}}>
                <h5 className="card-title">{item.name}</h5>
                <p className="card-text">{item.description}</p>
                <p className="card-text">Price: Ksh {item.price}</p>
                <button
                  className=""
                  onClick={() => handleOrderClick(item)}
                  style={{
                    backgroundColor: "red",
                    color: "white",
                    fontSize: "14px",
                    border:"none",
                    padding: "10px 20px",
                    borderRadius: "10px",
                  }}
                >
                  Order Now
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Modal */}
      {selectedItem && (
        <div
          className={`modal fade ${showModal ? "show" : ""}`}
          style={{ display: showModal ? "block" : "none" }}
        >
          <div className="modal-dialog">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">{selectedItem.name}</h5>
                <button
                  type="button"
                  className="btn-close"
                  onClick={() => setShowModal(false)}
                ></button>
              </div>
              <div className="modal-body">
                <img
                  src={selectedItem.image_url}
                  alt={selectedItem.name}
                  id="circle"
                  style={{width:"400px"}}
                />
                <p>{selectedItem.description}</p>
                <p>Price: Ksh {selectedItem.price}</p>
                <p>
                  Order message: Your order for {selectedItem.name} has been
                  placed.
                </p>
              </div>
              <div className="modal-footer">
                <button
                  type="button"
                  className="btn btn-secondary"
                  onClick={() => setShowModal(false)}
                >
                  Close
                </button>
                <button
                  type="button"
                  className="btn btn-primary"
                  onClick={handleConfirmOrder}
                >
                  Confirm Order
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
      {showModal && <div className="modal-backdrop fade show"></div>}

      {/* Toast */}
      {selectedItem && showToast && (
        <div
          className="toast show"
          style={{
            position: "fixed",
            bottom: "20px",
            right: "20px",
            minWidth: "200px",
          }}
        >
          <div className="toast-header">
            <strong className="me-auto">Order Confirmed</strong>
          </div>
          <div className="toast-body">
            Thank you for ordering the {selectedItem.name}. Your order is on the
            way.
          </div>
        </div>
      )}
    </div>
    </div>
  );
}

export default RestaurantMenu;







