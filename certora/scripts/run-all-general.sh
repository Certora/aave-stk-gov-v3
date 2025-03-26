#CMN="--compilation_steps_only"


echo "******** Running: 20 ***************"
certoraRun $CMN certora/conf/token-v3-general-depth0.conf --rule delegateCorrectness \
           --msg "20::token-v3-general-depth0.conf:::delegateCorrectness"

echo "******** Running: 21 ***************"
certoraRun $CMN certora/conf/token-v3-general-depth0.conf --rule sumOfVBalancesCorrectness \
           --msg "21::token-v3-general-depth0.conf:::sumOfVBalancesCorrectness"
           
echo "******** Running: 22 ***************"
certoraRun $CMN certora/conf/token-v3-general-depth0.conf --rule sumOfVBalancesCorrectness_onlyClaimRewardsAndRedeem \
           --msg "22::token-v3-general-depth0.conf:::sumOfVBalancesCorrectness_onlyClaimRewardsAndRedeem"
           
echo "******** Running: 23 ***************"
certoraRun $CMN certora/conf/token-v3-general-depth0.conf --rule sumOfVBalancesCorrectness_onlyClaimRewardsAndRedeemOnBehalf \
           --msg "23::token-v3-general-depth0.conf:::sumOfVBalancesCorrectness_onlyClaimRewardsAndRedeemOnBehalf"
           
echo "******** Running: 24 ***************"
certoraRun $CMN certora/conf/token-v3-general.conf --rule sumOfPBalancesCorrectness \
           --msg "24::token-v3-general.conf:::sumOfPBalancesCorrectness"
           
echo "******** Running: 25 ***************"
certoraRun $CMN certora/conf/token-v3-general-depth0.conf --rule sumOfPBalancesCorrectness_onlyClaimRewardsAndRedeem \
           --msg "25::token-v3-general-depth0.conf:::sumOfPBalancesCorrectness_onlyClaimRewardsAndRedeem"
           
echo "******** Running: 26 ***************"
certoraRun $CMN certora/conf/token-v3-general-depth0.conf --rule sumOfPBalancesCorrectness_onlyClaimRewardsAndRedeemOnBehalf \
           --msg "26::token-v3-general-depth0.conf:::sumOfPBalancesCorrectness_onlyClaimRewardsAndRedeemOnBehalf"
           
echo "******** Running: 27 ***************"
certoraRun $CMN certora/conf/token-v3-general-depth0.conf --rule sumOfPBalancesCorrectness_onlyRedeem \
           --msg "27::token-v3-general-depth0.conf:::sumOfPBalancesCorrectness_onlyRedeem"
           
echo "******** Running: 28 ***************"
certoraRun $CMN certora/conf/token-v3-general-depth0.conf  --rule sumOfPBalancesCorrectness_onlyRedeemOnBehalf \
           --msg "28::token-v3-general-depth0.conf:::sumOfPBalancesCorrectness_onlyRedeemOnBehalf"
           
echo "******** Running: 29 ***************"
certoraRun $CMN certora/conf/token-v3-general-depth0.conf --rule transferDoesntChangeDelegationMode \
           --msg "29::token-v3-general-depth0.conf:::transferDoesntChangeDelegationMode"

