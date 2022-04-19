import { combineReducers } from '@reduxjs/toolkit';

import { reducer as screen } from './screen';
import { reducer as photos } from './photo';

export default combineReducers({ screen, photos });
