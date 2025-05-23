class Solution {
    public int minNumberOfHours(int initialEnergy, int initialExperience, int[] energy, int[] experience) {
        int trainingHours = 0;

        int totalEnergyRequired = 0;
        for (int i=0;i<energy.length;i++)
        totalEnergyRequired += energy[i];

        if (initialEnergy <= totalEnergyRequired) {
            trainingHours += (totalEnergyRequired - initialEnergy + 1);
        }
           

        for (int i = 0; i < experience.length; i++) {
            if (initialExperience <= experience[i]) {
                int train = experience[i] - initialExperience + 1;
                trainingHours += train;
                initialExperience += train;
            }
            initialExperience += experience[i];
        }

        return trainingHours;
    }
}