%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define real_name h5py

Summary: A Pythonic interface to the HDF5 binary data format
Name: python-%{real_name}
Version: 2.2.0
Release: 1%{?dist}
License: BSD
Group: Development/Libraries/Python
URL: http://www.h5py.org/

Source: http://h5py.googlecode.com/files/h5py-2.2.0.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  gcc
BuildRequires:  python >= 2.6
BuildRequires:  hdf5-devel >= 1.8.3
BuildRequires:  python-devel >= 2.6
BuildRequires:  numpy
Requires:  python >= 2.6
Requires:  hdf5 >= 1.8.3
Requires:  hdf5-devel >= 1.8.3
Requires:  numpy

%description
H5py provides a simple, robust read/write interface to HDF5 data from Python.
Existing Python and Numpy concepts are used for the interface; for example,
datasets on disk are represented by a proxy class that supports slicing, and
has dtype and shape attributes. HDF5 groups are presented using a dictionary
metaphor, indexed by name.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.rst
%{python_sitearch}/%{real_name}/
%{python_sitearch}/*.egg-info

%changelog
* Thu Nov 28 2013 Chris LeBlanc <crleblanc@gmail.com> - 2.2.0-1
- Initial package (basic build, no support for parallel I/O)
