export const LOAD_PINS = 'pinsReducer/loadPins'
export const LOAD_BOARD_PINS = 'pinsReducer/loadBoardPins'

export const loadPins = (pins) => ({
    type: LOAD_PINS,
    pins
})

export const loadBoardPins = (boardPins) => ({
    type: LOAD_BOARD_PINS,
    boardPins
})


export const getAllPins = (query) => async (dispatch) => {
    let res;
    if (query) {
        res = await fetch(`/api/pins?${query}`)
    } else {
        res = await fetch(`/api/pins`)
    }
    if (res.ok) {
        const allPins = await res.json();
        const allPinArray = Object.values(allPins)

        dispatch(loadPins(allPinArray))
    } else {
        const errors = await res.json();
        return errors;
    }
}

export const getBoardPins = (id) => async (dispatch) => {
    let res;
    if (id) {
        res = await fetch(`/api/boards/${id}/pins`)
        if (res.ok) {
            const boardPins = await res.json();
            const boardPinArray = Object.values(boardPins)
            boardPinArray.map(
                async (btp) => {
                    res = await fetch(`/api/pins/${btp.pinId}`)
                    btp.pin = await res.json()
                })
            dispatch(loadBoardPins(boardPinArray))
        } else {
            const errors = await res.json();
            return errors;
        }
    }
}


const initialState = {};
export const pinsReducer = (state = initialState, action) => {
    let newState = { ...state }
    switch (action.type) {
        case LOAD_PINS:
            return { ...state, pins: { ...action.pins }, boardPins: { ...state.boardPins } }
        case LOAD_BOARD_PINS:
            action.boardPins.forEach((boardPin) => {
                state.boardPins[boardPin.boardId] = boardPin
            })
            return { ...state, pins: { ...state.pins } }
        default:
            return state;
    }
}
