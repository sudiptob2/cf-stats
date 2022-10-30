# Codeforces Stat Visualization

<a href="https://github.com/sudiptob2/cf-stats">
<img src="https://raw.githubusercontent.com/sudiptob2/cf-stats/main/output/light_card.svg#gh-dark-mode-only" />
<img src="https://raw.githubusercontent.com/sudiptob2/cf-stats/main/output/light_card.svg" />
</a>
<br/>
<a href="https://github.com/sudiptob2/cf-stats">
<img src="https://raw.githubusercontent.com/sudiptob2/cf-stats/main/output/max_rating.svg" />
<img src="https://raw.githubusercontent.com/sudiptob2/cf-stats/main/output/rating.svg" />
</a>

# Installation

### For step-by-step screenshots go [here](docs/INSTALLATIONSTEPS.md) 
### Video Demonstration
  - [Hindi](https://www.youtube.com/watch?v=lPASqH0ZoIc)

1. Star this repository :pray:
2. Create a copy of this repository by clicking
   [here](https://github.com/sudiptob2/cf-stats/generate). Note: this is
   **not** the same as forking a copy because it copies everything fresh,
   without the huge commit history.
3. Goto [config/.env.template](config/.env.template) and put your codeforces handle in the `CF_HANDLE` key.
4. Go to the [Actions Page](../../actions?query=workflow%3A"Generate+Stats+Images") and press "Run Workflow" on the
   right side of the screen to generate images for the first time.
    - The images will be automatically regenerated every 24 hours, but they can
      be regenerated manually by running the workflow this way.
5. Take a look at the images that have been created in the
   [`output`](output) folder.
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

# Contribution guideline

If you like this project and want to improve by adding features, fixing bugs or anything, please follow
the [contributing guidelines](docs/CONTRIBUTING.md).

# Acknowledgments

### Contributors List

- [Sudipto](https://github.com/sudiptob2)
- [Nazmul](https://github.com/nazmulweb)
- [Manish](https://github.com/csemanish12)

### Inspiration
This project is heavily inspired by [github-stats](https://github.com/jstrieb/github-stats) project
