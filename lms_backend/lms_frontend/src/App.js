import React from 'react';
import './App.css';
import Sidebar from './components/Sidebar';
import MainContent from './components/MainContent';
import Profile from './components/Profile';

function App() {
    return (
        <div className="app">
            <Sidebar />
            <MainContent />
            <Profile />
        </div>
    );
}

export default App;
