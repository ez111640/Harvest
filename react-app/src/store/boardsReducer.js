export const LOAD_BOARDS = 'boardsReducer/loadBoards'
export const LOAD_BOARD = 'boardsReducer/'

export const loadBoards = (boards) => ({
    type: LOAD_BOARDS,
    boards
})

export const loadBoard = (board) => ({
    type: LOAD_BOARD,
    board
})


export const getUserBoards = () => async (dispatch) => {
    let res = await fetch(`/api/boards`)
    if (res.ok) {
        const allBoards = await res.json();
        const allBoardArray = Object.values(allBoards)
        dispatch(loadBoards(allBoardArray))
    } else {
        const errors = await res.json();
        return errors;
    }
}

export const getBoardDetails = (board) => async (dispatch) => {
    if (board.id !== undefined) {
        let res = await fetch(`/api/boards/${board.id}/pins`)
        if (res.ok) {
            const pins = await res.json()
            const pinArray = Object.values(pins)
            board.pins = [...pinArray]
            dispatch(loadBoard(board))
        } else {
            const errors = await res.json();
            return errors;
        }
    }
}

const initialState = {
};
export const boardsReducer = (state = initialState, action) => {
    let newState = { ...state }
    switch (action.type) {
        case LOAD_BOARDS:
            return { ...state, ...action.boards  }
        default:
            return state;
    }
}
