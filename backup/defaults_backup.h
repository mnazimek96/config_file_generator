/*
*defaults.h
*
*
*generated on: 13/08/2020 13:25:14
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

const static struct DEF_value configParamsDefaults[CONFIG_PARAMETER_SIZE]=
{
	{DGN_CONF_OPEN_SPEED			,500    ,5000       ,2200   ,237    },
	{DGN_CONF_CLOSE_SPEED			,500    ,5000       ,1600   ,237    },
	{DGN_CONF_OPEN_TIME				,0      ,65535      ,1600   ,237    },
	{DGN_CONF_MAX_CURRENT			,800    ,6000       ,1600   ,237    },
	{DGN_CONF_OBSTR_CURRENT_O		,0      ,3000       ,1600   ,237    },
	{DGN_CONF_OBSTR_CURRENT_C		,0      ,3000       ,1600   ,237    },
	{DGN_CONF_CLOSE_TIMEOUT			,4000   ,65535      ,1600   ,237    },
	{DGN_CONF_MAX_DOOR_POS			,4000   ,65535      ,1600   ,237    },
	{DGN_CONF_EDGE_SENS_ACTIVE		,500    ,5000       ,1600   ,237    },
	{DGN_CONF_EDGE_SENS_VOLTAGE		,0      ,4          ,1600   ,237    },
	{DGN_CONF_CALIB_FREQ			,0      ,5000       ,1600   ,237    },
	{DGN_CONF_CLOSE_ATTEMPTS		,0      ,65535      ,1600   ,237    },
	{DGN_CONF_OPEN_ATTEMPTS			,0      ,65535      ,1600   ,237    },
	{DGN_CONF_MAX_SPEED				,0      ,65535      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,2000   ,10000      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,65535      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,65535      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,65535      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,300    ,4000       ,1600   ,237    },
	{DGN_SPARE_0					,0      ,0          ,0      ,0      },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,2          ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,2          ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,2          ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,2          ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,2          ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,2          ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,3          ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,3          ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,2          ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,1900       ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,200        ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,1000       ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,1000       ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,10     ,1500       ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,50     ,10000      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,-200   ,200        ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,10     ,95         ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,10     ,95         ,1600   ,237    },
	{DGN_ADV_SPARE_1				,0      ,0          ,0      ,0      },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,500        ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,101        ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,300    ,4000       ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,300    ,4000       ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,10     ,500        ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,300    ,2000       ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,300    ,2000       ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,101        ,1600   ,237    },
	{DGN_ADV_SPARE_2				,0      ,0          ,0      ,0      },
	{DGN_ADV_SPARE_3				,0      ,0          ,0      ,0      },
	{DGN_ADV_SPARE_4				,0      ,0          ,0      ,0      },
	{DGN_ADV_SPARE_5				,0      ,0          ,0      ,0      },
	{DGN_ADV_SPARE_6				,0      ,0          ,0      ,0      },
	{DGN_ADV_SPARE_7				,0      ,0          ,0      ,0      },
	{DGN_ADV_SPARE_8				,0      ,0          ,0      ,0      },
	{DGN_MIN_DEPLOYMENT_POS			,300    ,2000       ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,300        ,1600   ,237    },
	{DGN_CAL_SPARE1					,0      ,0          ,0      ,0      },
	{DGN_CAL_SPARE2					,0      ,0          ,0      ,0      },
	{DGN_MIN_DEPLOYMENT_POS			,300    ,6000       ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,300    ,6000       ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,100    ,4000       ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,100    ,4000       ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,2000       ,1600   ,237    },
	{DGN_CAL_SPARE0					,0      ,0          ,0      ,0      },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,65535      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,65535      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,65535      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,65535      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,65535      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,65535      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,65535      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,65535      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,65535      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,65535      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,65535      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,65535      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,65535      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,65535      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,65535      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,65535      ,1600   ,237    },
	{DGN_SPARE_1					,0      ,0          ,0      ,0      },
	{DGN_SPARE_2					,0      ,0          ,0      ,0      },
	{DGN_SPARE_3					,0      ,0          ,0      ,0      },
	{DGN_SPARE_4					,0      ,0          ,0      ,0      },
	{DGN_SPARE_5					,0      ,0          ,0      ,0      },
	{DGN_SPARE_6					,0      ,0          ,0      ,0      },
	{DGN_SPARE_7					,0      ,0          ,0      ,0      },
	{DGN_SPARE_8					,0      ,0          ,0      ,0      },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,65535      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,65535      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,65535      ,1600   ,237    },
	{DGN_MIN_DEPLOYMENT_POS			,0      ,65535      ,1600   ,237    },
};

#else
#error "defaults.h file should be included only once!"
#endif /* DEFAULTS_H_ */