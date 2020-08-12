/*
*defaults.h
*
*
*generated on: 12/08/2020 14:47:00
*Author: mnazimek
*/

#ifndef DEFAULTS_H_
#define DEFAULTS_H_

/* Two important infos:
* ->  This header should be included only in configuration.c file
* ->  Must include configuration.h and GENERAL_CONFIG.h before this one */

struct DEF_value {
	unit8_t id;
	int16_t def_val;
	int16_t range_max;
	int16_t range_min;
	unit8_t rw;
};

#define CONFIG_PARAMETER_SIZE 92

#else
#error "defaults.h file should be included only once!"
#endif /* DEFAULTS_H_ */