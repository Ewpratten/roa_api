# Public Route Origin Authorization API

This is the repository for `roa.va3zza.com`, a public tool that auto-generates [Bird2](https://bird.network.cz/)-style [ROA](https://www.arin.net/resources/manage/rpki/roa_request/) data for IP space that doesn't play nice with standard IRR tools.

Currently, the following networks are supported:

- [AMPRNet](https://www.ampr.org/)
  - [`roa.va3zza.com/api/amprnet`](https://roa.va3zza.com/api/amprnet)
- [DN42](https://dn42.eu)
  - [`roa.va3zza.com/api/dn42_ipv4`](https://roa.va3zza.com/api/dn42_ipv4)
  - [`roa.va3zza.com/api/dn42_ipv6`](https://roa.va3zza.com/api/dn42_ipv6)

## Using this data

Add a cron entry to pull your endpoint(s) of choice into some file in `/etc/bird/roa`, then you can load it as follows:

```text
protocol static {
    roa4 { table roa_v4; };
    include "/etc/bird/roa/amprnet.conf";
    include "/etc/bird/roa/dn42_ipv4.conf";
};

protocol static {
    roa6 { table roa_v6; };
    include "/etc/bird/roa/dn42_ipv6.conf";
};
```

From here, the standard Bird tools work as usual for validating prefixes.
