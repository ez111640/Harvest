import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux"
import { boardsReducer, getUserBoards } from "../../../store/boardsReducer"
import { BoardCard } from "./BoardCard/BoardCard";
import { getAllPins } from "../../../store/pinsReducer";
import {Link} from 'react-router-dom'
import "./UserBoards.css"



export const UserBoards = () => {
    const userBoards = useSelector((state) => state.boardsReducer)
    const dispatch = useDispatch();

    window.onbeforeunload = function() {
        window.setTimeout(function () {
            window.location = '/';
        }, 0);
        window.onbeforeunload = null; // necessary to prevent infinite loop, that kills your browser
    }

    useEffect(() => {
        dispatch(getUserBoards())
        dispatch(getAllPins())
    }, [dispatch])

    const userBoardArray = Object.values(userBoards)
    console.log("USERBOARDARRAY", userBoardArray)

    if (!userBoardArray.length) return null
    return (
        <div className="user-board-listing">
            {userBoardArray.map(
                (board) => (
                    <div>
                        <Link to={`/boards/${board.id}`}><BoardCard boardId={board.id} /></Link>
                        <div className="board-name">{board.name}</div>
                    </div>
                )

            )}
        </div>
    )
}
