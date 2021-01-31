import { createStore } from 'redux';
import Reducers from './reducers/index';

const Store = createStore(Reducers);


export default Store;