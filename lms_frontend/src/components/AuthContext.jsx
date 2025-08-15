import React,{useState} from "react";
import axios from "axios";
import { AuthContext } from "./AuthContext";

export function AuthProvider({children}){
    const [token,setToken]=useState(localStorage.getItem("token")||"");
    const [page,setPage]=useState(token? "profile":"login");

    const login=async(username,password)=>{
        const res=await axios.post("http://127.0.0.1:8000/api/token/",{username,password});
        const data=res.data;
        setToken(data.access);
        localStorage.setItem("token",data.token);
        setPage("profile"); 
    }
    const logout=()=>{
        setToken("");
        localStorage.removeItem("token")
        setPage("login")
    }
}