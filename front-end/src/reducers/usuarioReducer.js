
const INITIAL_STATE = {
    usuarioLogado: 0,
    usuarioEmail:null
}

function usuarioReducer(state = INITIAL_STATE, action){
    switch (action.type){
        case 'LOG_IN':
            return {
                ...state,
                usuarioLogado: 1,
                usuarioEmail: action.payload.usuarioEmail
            };
        case 'LOG_OUT':
            return {
                ...state,
                usuarioLogado: 0,
                usuarioEmail: null
            };
        default:{
                return state 
            }
    }
}

export default usuarioReducer;