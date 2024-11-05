import React from "react";
import './../assets/styles/Sidebar.css'

const Sidebar = () => {
    return (
        <div className="sidebar">
            <div className="logo">
                Academy
            </div>
            <ul>
                <li>Dashboard</li>
                <li>Courses</li> 
                <li>Chats</li>
                <li>Grades</li>
                <li>Schedule</li>
                <li>Settings</li>
            </ul>
        </div>
    )
}

export default Sidebar;