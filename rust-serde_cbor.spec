# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate serde_cbor

Name:           rust-%{crate}
Version:        0.10.2
Release:        2%{?dist}
Summary:        CBOR support for serde

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/serde_cbor
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
CBOR support for serde.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages
which use "alloc" feature of "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+unsealed_read_write-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unsealed_read_write-devel %{_description}

This package contains library source intended for building other packages
which use "unsealed_read_write" feature of "%{crate}" crate.

%files       -n %{name}+unsealed_read_write-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 09:43:03 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.2-1
- Update to 0.10.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 23:36:36 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.0-4
- Regenerate

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.0-2
- Adapt to new packaging

* Sat Sep 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Josh Stone <jistone@redhat.com> - 0.8.2-1
- Update to 0.8.2

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-2
- Rebuild for rust-packaging v5

* Tue Jan 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1

* Tue Nov 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1

* Wed Jul 05 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.0-1
- Initial package
