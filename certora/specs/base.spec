using DummyERC20Impl as stake_token;
using DummyERC20Impl as reward_token;

methods {

    function stake_token.balanceOf(address) external returns (uint256) envfree;

    // public variables
    function REWARDS_VAULT() external returns (address) envfree;
    function UNSTAKE_WINDOW() external returns (uint256) envfree;
    function LOWER_BOUND() external returns (uint256) envfree;
    //    function INITIAL_EXCHANGE_RATE() external returns (uint216) envfree;

    // envfree
    function balanceOf(address) external returns (uint256) envfree;
    function cooldownAmount(address) external returns (uint216) envfree;
    function cooldownTimestamp(address) external returns (uint40) envfree;
    function totalSupply() external returns (uint256) envfree;
    function stakerRewardsToClaim(address) external returns (uint256) envfree;
    function stakersCooldowns(address) external returns (uint40, uint216) envfree;
    function getCooldownSeconds() external returns (uint256) envfree;
    function getExchangeRate() external returns (uint216) envfree;
    function inPostSlashingPeriod() external returns (bool) envfree;
    function getMaxSlashablePercentage() external returns (uint256) envfree;
    function getAssetGlobalIndex(address) external returns (uint256) envfree;
    function getUserPersonalIndex(address, address) external returns (uint256) envfree;
    function previewStake(uint256) external returns (uint256) envfree;
    function previewRedeem(uint256) external returns (uint256) envfree;
    function getUserAssetData(address user, address asset) external returns (uint256) envfree;

    function _.permit(address, address, uint256, uint256, uint8, bytes32, bytes32) external => NONDET;
    function _.permit(address, address, uint256, uint256, uint8, bytes32, bytes32) internal => NONDET;

    // address, block, delegation type
    //function _votingSnapshotsCounts(address) external returns (uint256) envfree;
    //function _updateCurrentUnclaimedRewards(address, uint256, bool) external returns (uint256) envfree;

    // view but not envfree - uses block.timestamp
    function getNextCooldownTimestamp(uint256,uint256,address,uint256) external;
    function getPowerAtBlock(address,uint256,uint8) external returns (uint256);

    // state changing operations
    function initialize(address,address,address,uint256,uint256) external;
    function stake(address,uint256) external;
    function redeem(address,uint256) external;
    function slash(address,uint256) external returns (uint256);
    function returnFunds(uint256) external;

    // variable debt token
    function _.updateDiscountDistribution(address, address, uint256, uint256, uint256) external => NONDET;
}

methods {
    function totalSupply()                         external returns (uint256)   envfree;
    function balanceOf(address)                    external returns (uint256)   envfree;
    function allowance(address,address)            external returns (uint256)   envfree;
    function increaseAllowance(address, uint256) external;
    function decreaseAllowance(address, uint256) external;
    function transfer(address,uint256) external;
    function transferFrom(address,address,uint256) external;
    function permit(address,address,uint256,uint256,uint8,bytes32,bytes32) external;

    function delegate(address delegatee) external;
    function metaDelegate(address,address,uint256,uint8,bytes32,bytes32) external;
    function metaDelegateByType(address,address,uint8,uint256,uint8,bytes32,bytes32) external;
    function getPowerCurrent(address, IGovernancePowerDelegationToken.GovernancePowerType) external returns (uint256) envfree;

    function getBalance(address user) external returns (uint104) envfree;
    function getDelegatedPropositionBalance(address user) external returns (uint72) envfree;
    function getDelegatedVotingBalance(address user) external returns (uint72) envfree;
    function getDelegatingProposition(address user) external returns (bool) envfree;
    function getDelegatingVoting(address user) external returns (bool) envfree;
    function getVotingDelegatee(address user) external returns (address) envfree;
    function getPropositionDelegatee(address user) external returns (address) envfree;
    function getDelegationMode(address user) external returns (StakedAaveV3Harness.DelegationMode) envfree;

    function EXCHANGE_RATE_UNIT() external returns (uint256) envfree;
}

definition VOTING_POWER() returns IGovernancePowerDelegationToken.GovernancePowerType = IGovernancePowerDelegationToken.GovernancePowerType.VOTING;
definition PROPOSITION_POWER() returns IGovernancePowerDelegationToken.GovernancePowerType = IGovernancePowerDelegationToken.GovernancePowerType.PROPOSITION;
definition FACTOR() returns uint256 = 10^10; // This is the POWER_SCALE_FACTOR

/**
    Definitions of delegation modes
*/
definition NO_DELEGATION() returns StakedAaveV3Harness.DelegationMode = StakedAaveV3Harness.DelegationMode.NO_DELEGATION;
definition VOTING_DELEGATED() returns StakedAaveV3Harness.DelegationMode = StakedAaveV3Harness.DelegationMode.VOTING_DELEGATED;
definition PROPOSITION_DELEGATED() returns StakedAaveV3Harness.DelegationMode = StakedAaveV3Harness.DelegationMode.PROPOSITION_DELEGATED;
definition FULL_POWER_DELEGATED() returns StakedAaveV3Harness.DelegationMode = StakedAaveV3Harness.DelegationMode.FULL_POWER_DELEGATED;
definition DELEGATING_VOTING(StakedAaveV3Harness.DelegationMode mode) returns bool =
    mode == VOTING_DELEGATED() || mode == FULL_POWER_DELEGATED();
definition DELEGATING_PROPOSITION(StakedAaveV3Harness.DelegationMode mode) returns bool =
    mode == PROPOSITION_DELEGATED() || mode == FULL_POWER_DELEGATED();

definition SCALED_MAX_SUPPLY() returns mathint = AAVE_MAX_SUPPLY() / FACTOR();

definition AAVE_MAX_SUPPLY() returns uint256 = 16000000 * 10^18;
//definition EXCHANGE_RATE_FACTOR() returns uint256 = 10^18;
definition EXCHANGE_RATE_FACTOR() returns uint256 = EXCHANGE_RATE_UNIT();
definition PERCENTAGE_FACTOR() returns uint256 = 10^4;

// a reasonable assumption that slashing is below 99%
definition MAX_EXCHANGE_RATE() returns uint256 = 100 * 10^18;
definition MAX_PERCENTAGE() returns mathint = 100 * PERCENTAGE_FACTOR();
definition INITIAL_EXCHANGE_RATE_F() returns uint216 = 10^18;
definition MAX_COOLDOWN() returns uint256 = 2302683158; //20 years from now

definition claimRewards_funcs(method f) returns bool =
(
    f.selector == sig:claimRewards(address, uint256).selector ||
    f.selector == sig:claimRewardsOnBehalf(address, address, uint256).selector ||
    f.selector == sig:claimRewardsAndStake(address, uint256).selector ||
    f.selector == sig:claimRewardsAndStakeOnBehalf(address, address, uint256).selector ||
    f.selector == sig:claimRewardsAndRedeem(address, uint256, uint256).selector ||
    f.selector == sig:claimRewardsAndRedeemOnBehalf(address, address, uint256, uint256).selector
);

definition redeem_funcs(method f) returns bool =
(
    f.selector == sig:redeem(address, uint256).selector ||
    f.selector == sig:redeemOnBehalf(address, address, uint256).selector ||
    f.selector == sig:claimRewardsAndRedeem(address, uint256, uint256).selector ||
    f.selector == sig:claimRewardsAndRedeemOnBehalf(address, address, uint256, uint256).selector
);

//function normalize(uint256 amount) returns mathint {
//    return (amount / FACTOR() * FACTOR());
//}
definition norm(uint256 amount) returns mathint = 
    amount / FACTOR() * FACTOR();

function upto_1(mathint a, mathint b) returns bool {
    return  a==b  ||  a==b+1  ||  a+1==b;
}

function upto_2(mathint a, mathint b) returns bool {
    return  a==b  ||  a==b+1  ||  a==b+2  ||  a==b-1  ||  a==b-2;
}

function convert_to_power(mathint amount) returns mathint {
    return amount * EXCHANGE_RATE_FACTOR() / getExchangeRate();
}

function validDelegationMode(address user) returns bool {
    StakedAaveV3Harness.DelegationMode state = getDelegationMode(user);
    return state == StakedAaveV3Harness.DelegationMode.NO_DELEGATION ||
        state == StakedAaveV3Harness.DelegationMode.VOTING_DELEGATED ||
        state == StakedAaveV3Harness.DelegationMode.PROPOSITION_DELEGATED ||
        state == StakedAaveV3Harness.DelegationMode.FULL_POWER_DELEGATED;
}

function validAmount(uint256 amt) returns bool {
    return amt < AAVE_MAX_SUPPLY();
}

definition is_redeem_method(method f) returns bool =
    (
     f.selector == sig:redeem(address,uint256).selector ||
     f.selector == sig:redeemOnBehalf(address,address,uint256).selector ||
     f.selector == sig:claimRewardsAndRedeem(address,uint256,uint256).selector ||
     f.selector == sig:claimRewardsAndRedeemOnBehalf(address,address,uint256,uint256).selector
    );

definition is_stake_method(method f) returns bool =
    (
     f.selector == sig:stake(address,uint256).selector ||
     f.selector == sig:stakeWithPermit(uint256,uint256,uint8,bytes32,bytes32).selector ||
     f.selector == sig:claimRewardsAndStake(address,uint256).selector ||
     f.selector == sig:claimRewardsAndStakeOnBehalf(address,address,uint256).selector
    );

definition is_transfer_method(method f) returns bool =
    (
     f.selector == sig:transfer(address,uint256).selector ||
     f.selector == sig:transferFrom(address,address,uint256).selector
    );



function is_transfer_method_func(method f) returns bool {
    return
        f.selector == sig:transfer(address,uint256).selector ||
        f.selector == sig:transferFrom(address,address,uint256).selector;
}



ghost uint216 mirror_currentExchangeRate {
    init_state axiom mirror_currentExchangeRate==0;
}
hook Sstore _currentExchangeRate uint216 newVal (uint216 oldVal) STORAGE {
    mirror_currentExchangeRate = newVal;
}
hook Sload uint216 val _currentExchangeRate STORAGE {
    require(mirror_currentExchangeRate == val);
}


ghost mapping(address => mathint) sum_all_voting_delegated_power {
    init_state axiom forall address delegatee. sum_all_voting_delegated_power[delegatee] == 0;
}
ghost mapping(address => mathint) sum_all_proposition_delegated_power {
    init_state axiom forall address delegatee. sum_all_proposition_delegated_power[delegatee] == 0;
}

// =========================================================================
//   mirror_votingDelegatee
// =========================================================================
ghost mapping(address => address) mirror_votingDelegatee { 
    init_state axiom forall address a. mirror_votingDelegatee[a] == 0;
}
hook Sstore _votingDelegatee[KEY address delegator] address new_delegatee (address old_delegatee) STORAGE {
    mirror_votingDelegatee[delegator] = new_delegatee;
    if ((mirror_delegationMode[delegator]==FULL_POWER_DELEGATED() ||
         mirror_delegationMode[delegator]==VOTING_DELEGATED()) &&
        new_delegatee != old_delegatee) { // if a delegator changes his delegatee
        sum_all_voting_delegated_power[new_delegatee] =
            sum_all_voting_delegated_power[new_delegatee] +
            //NN(mirror_balance[delegator]);
            norm(mirror_balance[delegator]);
        sum_all_voting_delegated_power[old_delegatee] = 
            sum_all_voting_delegated_power[old_delegatee] -
            //NN(mirror_balance[delegator]);
            norm(mirror_balance[delegator]);
    }
}
hook Sload address val _votingDelegatee[KEY address delegator] STORAGE {
    require(mirror_votingDelegatee[delegator] == val);
}

// =========================================================================
//   mirror_propositionDelegatee
// =========================================================================
ghost mapping(address => address) mirror_propositionDelegatee { 
    init_state axiom forall address a. mirror_propositionDelegatee[a] == 0;
}
hook Sstore _propositionDelegatee[KEY address delegator] address new_delegatee (address old_delegatee) STORAGE {
    mirror_propositionDelegatee[delegator] = new_delegatee;
    if ((mirror_delegationMode[delegator]==FULL_POWER_DELEGATED() ||
         mirror_delegationMode[delegator]==PROPOSITION_DELEGATED()) &&
        new_delegatee != old_delegatee) { // if a delegator changes his delegatee
        sum_all_proposition_delegated_power[new_delegatee] =
            sum_all_proposition_delegated_power[new_delegatee] +
            //NN(mirror_balance[delegator]);
            norm(mirror_balance[delegator]);
        sum_all_proposition_delegated_power[old_delegatee] = 
            sum_all_proposition_delegated_power[old_delegatee] -
            //NN(mirror_balance[delegator]);
            norm(mirror_balance[delegator]);

    }
}
hook Sload address val _propositionDelegatee[KEY address delegator] STORAGE {
    require(mirror_propositionDelegatee[delegator] == val);
}

// =========================================================================
//   mirror_delegationMode
// =========================================================================
ghost mapping(address => StakedAaveV3Harness.DelegationMode) mirror_delegationMode { 
    init_state axiom forall address a. mirror_delegationMode[a] ==
        StakedAaveV3Harness.DelegationMode.NO_DELEGATION;
}
hook Sstore _balances[KEY address a].delegationMode StakedAaveV3Harness.DelegationMode newVal (StakedAaveV3Harness.DelegationMode oldVal) STORAGE {
    mirror_delegationMode[a] = newVal;

    if ( (newVal==VOTING_DELEGATED() || newVal==FULL_POWER_DELEGATED())
         &&
         (oldVal!=VOTING_DELEGATED() && oldVal!=FULL_POWER_DELEGATED())
       ) { // if we start to delegate VOTING now
        sum_all_voting_delegated_power[mirror_votingDelegatee[a]] =
            sum_all_voting_delegated_power[mirror_votingDelegatee[a]] +
            //NN(mirror_balance[a]);
            norm(mirror_balance[a]);
    }

    if ( (newVal==PROPOSITION_DELEGATED() || newVal==FULL_POWER_DELEGATED())
         &&
         (oldVal!=PROPOSITION_DELEGATED() && oldVal!=FULL_POWER_DELEGATED())
       ) { // if we start to delegate PROPOSITION now
        sum_all_proposition_delegated_power[mirror_propositionDelegatee[a]] =
            sum_all_proposition_delegated_power[mirror_propositionDelegatee[a]] +
            //NN(mirror_balance[a]);
            norm(mirror_balance[a]);
    }
}
hook Sload StakedAaveV3Harness.DelegationMode val _balances[KEY address a].delegationMode STORAGE {
    require(mirror_delegationMode[a] == val);
}


// =========================================================================
//   mirror_balance
// =========================================================================
ghost mapping(address => uint104) mirror_balance { 
    init_state axiom forall address a. mirror_balance[a] == 0;
}
hook Sstore _balances[KEY address a].balance uint104 balance (uint104 old_balance) STORAGE {
    mirror_balance[a] = balance;

    if (a!=0 &&
        (mirror_delegationMode[a]==FULL_POWER_DELEGATED() ||
         mirror_delegationMode[a]==VOTING_DELEGATED() )
        )
        sum_all_voting_delegated_power[mirror_votingDelegatee[a]] =
            sum_all_voting_delegated_power[mirror_votingDelegatee[a]] + 
            norm(balance) - norm(old_balance);

    if (a!=0 &&
        (mirror_delegationMode[a]==FULL_POWER_DELEGATED() ||
         mirror_delegationMode[a]==PROPOSITION_DELEGATED() )
        )
        sum_all_proposition_delegated_power[mirror_propositionDelegatee[a]] =
            sum_all_proposition_delegated_power[mirror_propositionDelegatee[a]] +
            norm(balance) - norm(old_balance);
}
hook Sload uint104 bal _balances[KEY address a].balance STORAGE {
    require(mirror_balance[a] == bal);
}
