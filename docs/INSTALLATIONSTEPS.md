# Installation
1. Star this repository :pray:

![star the repo](../assets/1.star-the-repo.png)

2. Create a copy of this repository by clicking
   [here](https://github.com/sudiptob2/cf-stats/generate). Note: this is
   **not** the same as forking a copy because it copies everything fresh,
   without the huge commit history.

![cloning the repo](../assets/2.clone-the-repo.png)

3. Goto [config/.env.template](../config/.env.template) and put your codeforces handle in the `CF_HANDLE` key.

![changing the env 1](../assets/3.change-env.png)

![changing the env 2](../assets/4.change.env.png)

![changing the env 3](../assets/5.change-handle.png)

4. Go to the [Actions Page](../../actions?query=workflow%3A"Generate+Stats+Images") and press "Run Workflow" on the
   right side of the screen to generate images for the first time.
    - As we updated the `CF_HANDLE` just now, so the workflow automatically ran.
   
![workflow run](../assets/6.workflow-run.png)
   
5. Take a look at the images that have been created in the
   [`output`](../output) folder.

![output images](../assets/7.output-folder.png)

6. To add your statistics to your GitHub Profile README, copy and paste the
   following lines of code into your markdown content. Change the `your-github-username`
   value to your GitHub username.

   ```md
   ![](https://raw.githubusercontent.com/your-github-username/cf-stats/main/output/light_card.svg#gh-dark-mode-only)
   ![](https://raw.githubusercontent.com/your-github-username/cf-stats/main/output/light_card.svg)
   ```
   ```md
   ![](https://raw.githubusercontent.com/sudiptob2/cf-stats/main/output/max_rating.svg)
   ![](https://raw.githubusercontent.com/sudiptob2/cf-stats/main/output/rating.svg)
   ```