 
within ProjektBuerogebaeude.Buerogebaeude.Buerogebaeude_DataBase;
record Buerogebaeude_006 "Buerogebaeude_006"
  extends AixLib.DataBase.ThermalZones.ZoneBaseRecord(
    T_start = 293.15,
    withAirCap = true,
    VAir = 357.04800000000006,
    AZone = 132.24,
    hRad = 5.0,
    lat = 0.88645272708792,
    nOrientations = 3,
    AWin = {0.0, 12.0, 12.0},
    ATransparent = {0.0, 12.0, 12.0},
    hConWin = 0.6000000000000002,
    RWin = 0.02631578947368421,
    gWin = 0.0,
    UWin= 1.1762624922614315,
    ratioWinConRad = 0.0,
    AExt = {31.59, 62.64, 29.655},
    hConExt = 2.7,
    nExt = 1,
    RExt = {0.00022037376960010326},
    RExtRem = 0.014578297040694393 ,
    CExt = {52077546.76886264},
    AInt = 534.1899987695201,
    hConInt = 1.6999999999999997,
    nInt = 1,
    RInt = {4.7574125086703415e-05},
    CInt = {46543170.62263035},
    AFloor = 0.0,
    hConFloor = 0.0,
    nFloor = 1,
    RFloor = {0.00001},
    RFloorRem =  0.00001,
    CFloor = {0.00001},
    ARoof = 0.0,
    hConRoof = 0.0,
    nRoof = 1,
    RRoof = {0.00001},
    RRoofRem = 0.00001,
    CRoof = {0.00001},
    nOrientationsRoof = 1,
    tiltRoof = {0.0},
    aziRoof = {0.0},
    wfRoof = {0.0},
    aRoof = 0.0,
    aExt = 0.7,
    TSoil = 286.15,
    hConWallOut = 19.999999999999996,
    hRadWall = 5.0,
    hConWinOut = 20.0,
    hConRoofOut = 0.0,
    hRadRoof = 0.0,
    tiltExtWalls = {1.5707963267948966, 1.5707963267948966, 1.5707963267948966},
    aziExtWalls = {0.0, 1.5707963267948966, -1.5707963267948966},
    wfWall = {0.2549945513984744, 0.505630221576462, 0.23937522702506364},
    wfWin = {0.0, 0.4999999999999999, 0.4999999999999999},
    wfGro = 0,
    specificPeople = 0.3333333333333333,
    fixedHeatFlowRatePersons = 70,
    ratioConvectiveHeatPeople = 0.5,
    internalGainsMachinesSpecific = 2.0,
    internalGainsMoistureNoPeople = 0.5,
    activityDegree = 1.2,
    ratioConvectiveHeatMachines = 0.75,
    lightingPowerSpecific = 15.9,
    ratioConvectiveHeatLighting = 0.9,
    useConstantACHrate = false,
    baseACH = 0.2,
    maxUserACH = 1.0,
    maxOverheatingACH = {3.0, 2.0},
    maxSummerACH = {1.0, 283.15, 290.15},
    winterReduction = {0.2, 273.15, 283.15},
    maxIrr = {9999.9, 0.0, 0.0},
    shadingFactor = {1.0, 1.0, 1.0},
    withAHU = false,
    minAHU = 0.0,
    maxAHU = 12.0,
    hHeat = 10000,
    lHeat = 0,
    KRHeat = 100,
    TNHeat = 50,
    HeaterOn = true,
    hCool = 0,
    lCool = -10000,
    KRCool = 10000,
    TNCool = 1,
    CoolerOn = true,
    withIdealThresholds = false,
    TThresholdHeater = 288.15,
    TThresholdCooler = 295.15);
end Buerogebaeude_006;
