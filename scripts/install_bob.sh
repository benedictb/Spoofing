export PATH="$HOME/miniconda/bin:$PATH"
conda update -n root conda
conda config --set show_channel_urls True
conda config --add channels conda-forge
conda create -n bob_env_py27 python=2.7 bob
source activate bob_env_py27
