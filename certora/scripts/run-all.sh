CMN="--disable_auto_cache_key_gen"



echo "******** Running:  1 ***************"
certoraRun $CMN certora/conf/token-v3-delegate-HL-under-approx.conf \
           --rule vp_change_in_balance_affect_power_DELEGATEE_all_others

echo "******** Running:  2 ***************"
certoraRun $CMN  certora/conf/token-v3-delegate-HL-under-approx.conf \
           --rule vp_change_in_balance_affect_power_DELEGATEE_transfer_M

echo "******** Running:  3 ***************"
certoraRun $CMN  certora/conf/token-v3-delegate-HL-under-approx.conf \
           --rule vp_change_in_balance_affect_power_DELEGATEE_stake_M

echo "******** Running:  4 ***************"
certoraRun $CMN  certora/conf/token-v3-delegate-HL-under-approx.conf \
           --rule vp_change_in_balance_affect_power_DELEGATEE_redeem_M

echo "******** Running:  5 ***************"
certoraRun $CMN  certora/conf/token-v3-delegate-HL-under-approx.conf \
           --rule vp_change_in_balance_affect_power_DELEGATEE_delegate_M



echo "******** Running:  6 ***************"
certoraRun $CMN  certora/conf/token-v3-delegate-HL-under-approx.conf \
           --rule pp_change_in_balance_affect_power_DELEGATEE_all_others

echo "******** Running:  7 ***************"
certoraRun $CMN  certora/conf/token-v3-delegate-HL-under-approx.conf \
           --rule pp_change_in_balance_affect_power_DELEGATEE_transfer_M

echo "******** Running:  8 ***************"
certoraRun $CMN  certora/conf/token-v3-delegate-HL-under-approx.conf \
           --rule pp_change_in_balance_affect_power_DELEGATEE_stake_M

echo "******** Running:  9 ***************"
certoraRun $CMN  certora/conf/token-v3-delegate-HL-under-approx.conf \
           --rule pp_change_in_balance_affect_power_DELEGATEE_redeem_M

echo "******** Running: 10 ***************"
certoraRun $CMN  certora/conf/token-v3-delegate-HL-under-approx.conf \
           --rule pp_change_in_balance_affect_power_DELEGATEE_delegate_M



echo "******** Running: 11 ***************"
certoraRun $CMN  certora/conf/token-v3-delegate-HL.conf \
           --rule vp_change_of_balance_affect_power_NON_DELEGATEE

echo "******** Running: 12 ***************"
certoraRun $CMN  certora/conf/token-v3-delegate-HL.conf \
           --rule pp_change_of_balance_affect_power_NON_DELEGATEE

echo "******** Running: 13 ***************"
certoraRun $CMN certora/conf/token-v3-delegate-HL.conf \
           --rule \
           mirror_votingDelegatee_correct \
           mirror_propositionDelegatee_correct \
           mirror_delegationMode_correct \
           mirror_balance_correct \
           inv_voting_power_correct \
           inv_proposition_power_correct \
           user_cant_voting_delegate_to_himself \
           user_cant_proposition_delegate_to_himself \
           no_function_changes_both_balance_and_delegation_state \
           sum_all_voting_delegated_power_EQ_DelegatingVotingBal \
           sum_all_proposition_delegated_power_EQ_DelegatingPropositionBal


echo "******** Running: 14 ***************"
certoraRun $CMN certora/conf/token-v3-delegate.conf 

echo "******** Running: 15 ***************"
certoraRun $CMN certora/conf/allProps.conf \
           --rule integrityOfSlashing \
           --rule integrityOfStaking \
           --rule previewStakeEquivalentStake \
           --rule noStakingPostSlashingPeriod \
           --rule noSlashingMoreThanMax \
           --rule noRedeemOutOfUnstakeWindow \
           --rule noEntryUntilSlashingSettled \
           --rule integrityOfRedeem \
           --rule cooldownCorrectness \
           --rule airdropNotMutualized \
           --rule integrityOfReturnFunds \
           --rule rewardsIncreaseForNonClaimFunctions \
           --rule rewardsMonotonicallyIncrease \
           --rule rewardsGetterEquivalentClaim \
           --rule indexesMonotonicallyIncrease \
           --rule exchangeRateNeverZero \
           --rule totalSupplyDoesNotDropToZero \
           --rule slashingIncreaseExchangeRate \
           --rule returnFundsDecreaseExchangeRate \
           --msg "15. allProps.conf::  all rules"


echo "******** Running: 16 ***************"
certoraRun $CMN certora/conf/token-v3-erc20.conf 

echo "******** Running: 17 ***************"
certoraRun $CMN certora/conf/token-v3-community.conf 

echo "******** Running: 18 ***************"
certoraRun $CMN certora/conf/propertiesWithSummarization.conf 

echo "******** Running: 19 ***************"
certoraRun $CMN certora/conf/invariants.conf 


echo "******** Running: 20 ***************"
certoraRun $CMN certora/conf/token-v3-general.conf --rule delegateCorrectness
echo "******** Running: 21 ***************"
certoraRun $CMN certora/conf/token-v3-general.conf --rule sumOfVBalancesCorrectness
echo "******** Running: 22 ***************"
certoraRun $CMN certora/conf/token-v3-general.conf --rule sumOfVBalancesCorrectness_onlyClaimRewardsAndRedeem
echo "******** Running: 23 ***************"
certoraRun $CMN certora/conf/token-v3-general.conf --rule sumOfVBalancesCorrectness_onlyClaimRewardsAndRedeemOnBehalf
echo "******** Running: 24 ***************"
certoraRun $CMN certora/conf/token-v3-general.conf --rule sumOfPBalancesCorrectness
echo "******** Running: 25 ***************"
certoraRun $CMN certora/conf/token-v3-general.conf --rule sumOfPBalancesCorrectness_onlyClaimRewardsAndRedeem
echo "******** Running: 26 ***************"
certoraRun $CMN certora/conf/token-v3-general.conf --rule sumOfPBalancesCorrectness_onlyClaimRewardsAndRedeemOnBehalf
echo "******** Running: 27 ***************"
certoraRun $CMN certora/conf/token-v3-general.conf --rule sumOfPBalancesCorrectness_onlyRedeem
echo "******** Running: 28 ***************"
certoraRun $CMN certora/conf/token-v3-general.conf  --rule sumOfPBalancesCorrectness_onlyRedeemOnBehalf
echo "******** Running: 29 ***************"
certoraRun $CMN certora/conf/token-v3-general.conf --rule transferDoesntChangeDelegationMode




