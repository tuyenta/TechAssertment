##  ⚠️   Notes for candidates

You should have received our instructions laying out what's expected from you and how we will review it.

This is a fake repository and not a real production application that we use. We included a lot of wrong practices and misconfigurations on purpose. **Do no use this as a source of inspiration for your project!**

The rest of this README will be written as if it was a real application.

---

## Goal

This repo's goal is to ingest Nantes' public parking usage data. This is a proof-of-concept and I'm sure there are a lot of things to improve.

## Prerequisites

We use Docker. Make sure you have a recent version of Docker installed (as of writing, we use Docker 20.10.8).

## Getting the data

Download the data (this takes about 10 minutes):

```bash
curl 'https://data.nantesmetropole.fr/explore/dataset/244400404_parkings-publics-nantes-statistiques-occupation-2020/download/?format=json' -o data/parking-data.json
```

## Running the ingester

```bash
docker compose up --build
```