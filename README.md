To run this on any machine with a suitable GPU run.

```
sudo docker run -it --gpus=all --env API_KEY=<API_KEY> --env PROMPT_ZERO_URL=https://www.promptzero.com chitalian/promptzero-worker:0.0.1 bash -c "conda run --no-capture-output -n ldm python main.py"
```
