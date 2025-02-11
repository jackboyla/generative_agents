

# Generative Agents: Interactive Simulacra of Human Behavior 

<p align="center" width="100%">
<img src="cover.png" alt="Smallville" style="width: 80%; min-width: 300px; display: block; margin: auto;">
</p>

This repository contains the frontend from the repository "[generative_agents](https://github.com/joonspk-research/generative_agents)" that accompanies the paper "[Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442)."


## Setting Up The Environment

Do not change the env name to be able to use the bash scripts later.
```bash
conda create -n simulacra python=3.9.12 -y
conda activate simulacra
pip install -r requirements.txt
```

## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Klaus_Mueller.png" alt="Generative Klaus"> Running a simulation

```bash
./run_frontend.sh <PORT-NUMBER>
```

> [!NOTE] 
> Omit the port number to use the default 8000.


Your server will be running at [http://localhost:8000/](http://localhost:8000/)

## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Maria_Lopez.png" alt="Generative Maria"> Replaying a Simulation
You can replay a simulation that you have already run simply by having your environment server running and navigating to the following address in your browser:

```bash
http://localhost:8000/replay/<simulation-name>/<starting-time-step>
``` 
Please make sure to replace `<simulation-name>` with the name of the simulation you want to replay, and `<starting-time-step>` with the integer time-step from which you wish to start the replay.

For instance, by visiting the following link, you will initiate a pre-simulated example, starting at time-step 1:  
[http://localhost:8000/replay/July1_the_ville_isabella_maria_klaus-step-3-20/1/](http://localhost:8000/replay/July1_the_ville_isabella_maria_klaus-step-3-20/1/)


## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Wolfgang_Schulz.png" alt="Generative Wolfgang"> Customizing the Map

The default simulation map, "The Ville", is a small town with locations such as a college, apartments, a cafe, a market, etc. The full list of locations and objects in this map are contained in the following files: [`sector_blocks.csv`](environment/frontend_server/static_dirs/assets/the_ville/matrix/special_blocks/sector_blocks.csv), [`arena_blocks.csv`](environment/frontend_server/static_dirs/assets/the_ville/matrix/special_blocks/arena_blocks.csv), and [`game_object_blocks.csv`](environment/frontend_server/static_dirs/assets/the_ville/matrix/special_blocks/game_object_blocks.csv). These are organized in a rough hierarchy: sector blocks roughly define buildings, arena blocks define rooms in buildings, and game object blocks define objects or areas in rooms.

To fully overhaul the map for your own customized simulation, you'd probably need to use the Tiled map editor as described in the [original repo's README](README_origin.md). 

> For a more involved customization, you will need to author your own base simulation files. The most straightforward approach would be to copy and paste an existing base simulation folder, renaming and editing it according to your requirements. This process will be simpler if you decide to keep the agent names unchanged. However, if you wish to change their names or increase the number of agents that the Smallville map can accommodate, you might need to directly edit the map using the [Tiled](https://www.mapeditor.org/) map editor.

This repo has added a shortcut method of customizing the map: renaming locations and objects that already exist in the Ville map.

To use this feature, add a `block_remaps` property to your simulation's `meta.json` file. Here's an example of remapping the supply store to be a fire station instead:

```json
{
  "fork_sim_code": "base_the_ville_isabella_maria_klaus",
  "start_date": "February 13, 2023",
  "curr_time": "February 13, 2023, 00:00:00",
  "sec_per_step": 10,
  "maze_name": "the_ville",
  "persona_names": [
    "Isabella Rodriguez",
    "Maria Lopez",
    "Klaus Mueller"
  ],
  "step": 0,
  "block_remaps": {
    "sector": {
      "Harvey Oak Supply Store": "Fire station"
    },
    "arena": {
      "supply store": "fire station"
    },
    "game_object": {
      "supply store product shelf": "fire truck",
      "supply store counter": "common area",
      "behind the supply store counter": "bunks"
    }
  }
}
```

When using this feature, reference the existing blocks in the blocks CSVs listed above. **Make sure to spell and case everything exactly as they are in those files!**

After remapping locations and objects in `meta.json`, you'll also need to rename them in each agent's `spatial_memory.json` file too, if they're referenced. This file defines what locations the agent is already aware of when the simulation starts. For instance, here's a link to Isabella's spatial memory file for the `base_the_ville_isabella_maria_klaus` simulation: [`spatial_memory.json`](environment/frontend_server/storage/base_the_ville_isabella_maria_klaus/personas/Isabella%20Rodriguez/bootstrap_memory/spatial_memory.json). Also, if a particular location is referenced in an agent's `scratch.json`, you'll need to update that too: [`scratch.json`](environment/frontend_server/storage/base_the_ville_isabella_maria_klaus/personas/Isabella%20Rodriguez/bootstrap_memory/scratch.json).


## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Eddy_Lin.png" alt="Generative Eddy">   Authors and Citation 

**Authors:** Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein

Please cite our paper if you use the code or data in this repository. 
```
@inproceedings{Park2023GenerativeAgents,  
author = {Park, Joon Sung and O'Brien, Joseph C. and Cai, Carrie J. and Morris, Meredith Ringel and Liang, Percy and Bernstein, Michael S.},  
title = {Generative Agents: Interactive Simulacra of Human Behavior},  
year = {2023},  
publisher = {Association for Computing Machinery},  
address = {New York, NY, USA},  
booktitle = {In the 36th Annual ACM Symposium on User Interface Software and Technology (UIST '23)},  
keywords = {Human-AI interaction, agents, generative AI, large language models},  
location = {San Francisco, CA, USA},  
series = {UIST '23}
}
```