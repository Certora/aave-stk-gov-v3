// SPDX-License-Identifier: MIT

/**

  This is an extension of the harnessed AaveTokenV3 with added getters on the _balances fields.
  The imported harnessed AaveTokenV3 contract uses uint8 instead of an enum for delegation state.

  This modification is introduced to bypass a current Certora Prover limitation on accessing
  enum fields inside CVL hooks

 */

pragma solidity ^0.8.0;


import {StakedAaveV3} from '../../../src/contracts/StakedAaveV3.sol';
import {IERC20} from 'openzeppelin-contracts/contracts/token/ERC20/IERC20.sol';

import {DelegationMode} from 'aave-token-v3/DelegationAwareBalance.sol';
// For some reason, the solc compiler won't compile with the following line, instead of the above one.
// It's the same file !!!
//import {DelegationMode} from '../../../lib/aave-token-v3/src/DelegationAwareBalance.sol';

contract StakedAaveV3Harness is StakedAaveV3 {
    constructor(IERC20 stakedToken, IERC20 rewardToken, uint256 unstakeWindow, address rewardsVault,
                address emissionManager, uint128 distributionDuration)
        StakedAaveV3(stakedToken, rewardToken, unstakeWindow, rewardsVault,
                    emissionManager, distributionDuration) {}

    // Returns amount of the cooldown initiated by the user.
    function cooldownAmount(address user) public view returns (uint216) {
        return stakersCooldowns[user].amount;
    }

    // Returns timestamp of the cooldown initiated by the user.
    function cooldownTimestamp(address user) public view returns (uint40) {
        return stakersCooldowns[user].timestamp;
    }

    // Returns the asset's emission per second from the sturct
    function getAssetEmissionPerSecond(address token) public view returns (uint128) {
        return assets[token].emissionPerSecond;
    }

    // Returns the asset's last updated timestamp from the sturct
    function getAssetLastUpdateTimestamp(address token) public view returns (uint128) {
        return assets[token].lastUpdateTimestamp;
    }

    // Returns the asset's global index from the sturct
    function getAssetGlobalIndex(address token) public view returns (uint256) {
        return assets[token].index;
    }

    // Returns the user's personal index for the specific asset
    function getUserPersonalIndex(address token, address user) public view returns (uint256) {
        return assets[token].users[user];
    }

    function _getExchangeRateWrapper(uint256 totalAssets, uint256 totalShares) public pure returns (uint216) {
        return _getExchangeRate(totalAssets, totalShares);
    }

    


    
    function getBalance(address user) public view returns (uint104) {
        return _balances[user].balance;
    }
    
    function getDelegatedPropositionBalance(address user) public view returns (uint72) {
        return _balances[user].delegatedPropositionBalance;
    }
    
    function getDelegatedVotingBalance(address user) public view returns (uint72) {
        return _balances[user].delegatedVotingBalance;
    }
    
    function getDelegatingProposition(address user) public view returns (bool) {
        uint8 state = uint8(_balances[user].delegationMode);
        return
            state == uint8(DelegationMode.PROPOSITION_DELEGATED) ||
            state == uint8(DelegationMode.FULL_POWER_DELEGATED);
    }
    
    function getDelegatingVoting(address user) public view returns (bool) {
        uint8 state = uint8(_balances[user].delegationMode);
        return
            state == uint8(DelegationMode.VOTING_DELEGATED) ||
            state == uint8(DelegationMode.FULL_POWER_DELEGATED);
    }
    
    function getVotingDelegate(address user) public view returns (address) {
        return _votingDelegatee[user];
    }
    
    function getPropositionDelegate(address user) public view returns (address) {
        return _propositionDelegatee[user];
    }
    
    function getDelegationMode(address user) public view returns (DelegationMode) {
        DelegationMode d = _balances[user].delegationMode;
        return d;
    }
}

