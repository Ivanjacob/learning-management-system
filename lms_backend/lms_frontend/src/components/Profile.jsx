import React from 'react';
import './../assets/styles/Profile.css';

const ProfileCard = () => {
    return (
        <div className="profile-card">
            <div className="profile">
                <img src="/path-to-avatar.jpg" alt="Profile" />
                <p>Esther Howard</p>
                <p>Elementary</p>
            </div>
            <div className="calendar">
                <h3>May 2022</h3>
                {/* Add calendar grid here */}
            </div>
        </div>
    );
}

export default ProfileCard;
