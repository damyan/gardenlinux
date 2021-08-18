def test_gcp_instances(gcp_cfg, compute_client):
    zones = compute_client.zones().list(project=gcp_cfg.project_id).execute()
    print('Getting all zones for this project:')
    for zone in zones['items']:
        print(f"Zone: {zone['name']=}, {zone['id']=}, {zone['status']}")

    zone = 'europe-west2-a'
    result = compute_client.instances().list(project=gcp_cfg.project_id, zone=zone).execute()
    assert(len(result) != 0)
    instances =  result['items'] if 'items' in result else []
    print(f'Getting instances for zone {zone}:')
    for instance in instances:
        print(' - ' + instance['name'])
