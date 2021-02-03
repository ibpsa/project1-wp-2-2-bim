 
within ProjektBuerogebaeude.Buerogebaeude.Buerogebaeude_DataBase;
record Buerogebaeude_009 "Buerogebaeude_009"
  extends AixLib.DataBase.ThermalZones.ZoneBaseRecord(
    T_start = 293.15,
    withAirCap = true,
    VAir = 34.452,
    AZone = 12.76,
    hRad = 5.0,
    lat = 0.88645272708792,
    nOrientations = 2,
    AWin = {3.0, 0.0},
    ATransparent = {3.0, 0.0},
    hConWin = 0.6,
    RWin = 0.21052631578947367,
    gWin = 0.0,
    UWin= 1.176262492261431,
    ratioWinConRad = 0.0,
    AExt = {0, 15.659999517186002},
    hConExt = 2.7,
    nExt = 1,
    RExt = {0.0017433592138331436},
    RExtRem = 0.11532773847817825 ,
    CExt = {6582995.175014089},
    AInt = 92.485,
    hConInt = 1.6999999999999997,
    nInt = 1,
    RInt = {0.0005497610859464839},
    CInt = {6910050.005358915},
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
    hConWallOut = 20.0,
    hRadWall = 5.0,
    hConWinOut = 20.0,
    hConRoofOut = 0.0,
    hRadRoof = 0.0,
    tiltExtWalls = {1.5707963267948966, 1.5707963267948966},
    aziExtWalls = {-1.5707963267948966, 3.141592653589793},
    wfWall = {0.0, 1.0},
    wfWin = {1.0, 0.0},
    wfGro = 0,
    specificPeople = 0.0,
    fixedHeatFlowRatePersons = 70,
    ratioConvectiveHeatPeople = 0.5,
    internalGainsMachinesSpecific = 0.0,
    internalGainsMoistureNoPeople = 10,
    activityDegree = 1.2,
    ratioConvectiveHeatMachines = 0.75,
    lightingPowerSpecific = 11.1,
    ratioConvectiveHeatLighting = 0.9,
    useConstantACHrate = false,
    baseACH = 0.2,
    maxUserACH = 1.0,
    maxOverheatingACH = {3.0, 2.0},
    maxSummerACH = {1.0, 283.15, 290.15},
    winterReduction = {0.2, 273.15, 283.15},
    maxIrr = {0.0, 9999.9},
    shadingFactor = {1.0, 1.0},
    withAHU = false,
    minAHU = 0.0,
    maxAHU = 8.0,
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
end Buerogebaeude_009;
